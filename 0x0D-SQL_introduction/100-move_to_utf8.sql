-- Alter the database to use UTF-8 (utf8mb4) encoding and utf8mb4_unicode_ci collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Alter the table first_table to use UTF-8 (utf8mb4) encoding and utf8mb4_unicode_ci collation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Alter the name field in first_table to use UTF-8 (utf8mb4) encoding and utf8mb4_unicode_ci collation
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
