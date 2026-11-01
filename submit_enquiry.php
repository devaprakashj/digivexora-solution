<?php
declare(strict_types=1);

// Receives the enquiry form (contact page and every service page) and saves it to MySQL.

function respond(string $message, bool $success = false, int $status = 400): never {
    http_response_code($status);
    header('X-Robots-Tag: noindex, nofollow');
    $safe = htmlspecialchars($message, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
    $heading = $success ? 'Thank you' : 'We could not send your enquiry';
    echo '<!doctype html><html lang="en"><head><meta charset="utf-8">'
       . '<meta name="viewport" content="width=device-width,initial-scale=1">'
       . '<meta name="robots" content="noindex,nofollow">'
       . '<title>' . $heading . ' | Digivexora Solution</title>'
       . '<link rel="icon" href="assets/favicon.ico"><link rel="stylesheet" href="style.css"></head><body>'
       . '<main><section class="band"><div class="wrap notice">'
       . '<img src="assets/logo-600.png" width="600" height="122" alt="Digivexora Solution logo" style="height:90px;width:auto;margin-bottom:28px">'
       . '<h1>' . $heading . '</h1><p class="lead">' . $safe . '</p>'
       . '<div class="actions"><a class="btn btn--primary" href="' . ($success ? 'index.html' : 'contact.html') . '">'
       . ($success ? 'Back to the home page' : 'Back to the form') . '</a></div>'
       . '</div></section></main></body></html>';
    exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Location: contact.html', true, 303);
    exit;
}

// Honeypot: real visitors never see or fill this field; bots often do.
if (!empty($_POST['website_url'] ?? '')) {
    respond('Your enquiry could not be processed. Please go back and try again.');
}

$name       = trim((string)($_POST['name'] ?? ''));
$phone      = trim((string)($_POST['phone'] ?? ''));
$business   = trim((string)($_POST['business'] ?? ''));
$email      = trim((string)($_POST['email'] ?? ''));
$service    = trim((string)($_POST['service'] ?? ''));
$message    = trim((string)($_POST['message'] ?? ''));
$sourcePage = trim((string)($_POST['source_page'] ?? ''));
$consent    = isset($_POST['consent']) ? 1 : 0;

// Keep only a safe file-name-like value for the page the form was sent from.
if (!preg_match('/^[a-z0-9\-]{1,100}\.html$/', $sourcePage)) {
    $sourcePage = null;
}

// Must match the options on the website forms exactly.
$allowedServices = [
    'Search Engine Optimization (SEO)',
    'Local SEO & Google Business Profile',
    'Social Media Management',
    'Meta Ads - Facebook & Instagram',
    'Google Ads (PPC)',
    'Website Design & Development',
    'Graphic Design & Poster Design',
    'Reels & Video Editing',
    'YouTube Channel Management',
    'Multiple services / Not sure yet',
];

if (mb_strlen($name) < 2 || mb_strlen($name) > 120) respond('Please enter your name (2 to 120 characters).');
if (!preg_match('/^[0-9+() .\-]{8,25}$/', $phone)) respond('Please enter a valid phone number.');
if ($email !== '' && (!filter_var($email, FILTER_VALIDATE_EMAIL) || mb_strlen($email) > 190)) respond('Please enter a valid email address.');
if (!in_array($service, $allowedServices, true)) respond('Please choose one of the listed services.');
if (!$consent) respond('Please confirm that we may contact you about this enquiry.');
if (mb_strlen($business) > 160 || mb_strlen($message) > 5000) respond('Some information is too long. Please shorten it and try again.');

$configPath = __DIR__ . '/config.php';
if (!is_file($configPath)) {
    respond('The form is not configured yet. Copy config.example.php to config.php and set up the database.', false, 500);
}
$config = require $configPath;

try {
    $dsn = sprintf('mysql:host=%s;dbname=%s;charset=utf8mb4', $config['host'], $config['database']);
    $pdo = new PDO($dsn, $config['username'], $config['password'], [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ]);
    $stmt = $pdo->prepare(
        'INSERT INTO enquiries (name, phone, business, email, service, message, source_page, consent)
         VALUES (:name, :phone, :business, :email, :service, :message, :source_page, :consent)'
    );
    $stmt->execute([
        ':name'        => $name,
        ':phone'       => $phone,
        ':business'    => $business !== '' ? $business : null,
        ':email'       => $email !== '' ? $email : null,
        ':service'     => $service,
        ':message'     => $message !== '' ? $message : null,
        ':source_page' => $sourcePage,
        ':consent'     => $consent,
    ]);
    respond('Your enquiry has been received. We will contact you using the details you provided.', true, 200);
} catch (Throwable $e) {
    error_log('Digivexora enquiry failed: ' . $e->getMessage());
    respond('Something went wrong while saving your enquiry. Please try again later or email us directly.', false, 500);
}
