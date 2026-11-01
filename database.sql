-- MySQL schema for Digivexora Solution website enquiries
CREATE DATABASE IF NOT EXISTS digivexora_db
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE digivexora_db;

CREATE TABLE IF NOT EXISTS enquiries (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(120) NOT NULL,
  phone VARCHAR(25) NOT NULL,
  business VARCHAR(160) NULL,
  email VARCHAR(190) NULL,
  service VARCHAR(120) NOT NULL,
  message TEXT NULL,
  source_page VARCHAR(100) NULL,
  consent TINYINT(1) NOT NULL DEFAULT 0,
  status ENUM('new','contacted','qualified','closed','spam') NOT NULL DEFAULT 'new',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_enquiries_created_at (created_at),
  INDEX idx_enquiries_status (status),
  INDEX idx_enquiries_service (service)
) ENGINE=InnoDB;

-- If you already imported the older schema, add the new column with:
-- ALTER TABLE enquiries ADD COLUMN source_page VARCHAR(100) NULL AFTER message;
