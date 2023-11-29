# planetbook

https://www.mockaroo.com


-- Table for Authors
CREATE TABLE authors (
    author_id INT PRIMARY KEY AUTO_INCREMENT,
    author_name VARCHAR(100) NOT NULL,
    biography TEXT,
    birth_date DATE,
    death_date DATE,
    nationality VARCHAR(50)
);

-- Table for Books
CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    isbn VARCHAR(20),
    genre VARCHAR(50),
    description TEXT,
    publication_date DATE,
    publisher VARCHAR(100),
    language VARCHAR(50),
    num_pages INT,
    edition VARCHAR(50),
    cover_image_url VARCHAR(255)
);

-- Table for Users
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    member_id VARCHAR(20),
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    membership_status VARCHAR(20)
);

-- Table for Borrowing and Returns
CREATE TABLE borrow_return (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    book_id INT,
    date_borrowed DATE,
    due_date DATE,
    date_returned DATE,
    fine DECIMAL(8, 2),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

-- Table for Library Staff
CREATE TABLE library_staff (
    staff_id INT PRIMARY KEY AUTO_INCREMENT,
    staff_name VARCHAR(100) NOT NULL,
    contact_information VARCHAR(255),
    role VARCHAR(50)
);

-- Table for Library Sections
CREATE TABLE library_sections (
    section_id INT PRIMARY KEY AUTO_INCREMENT,
    section_name VARCHAR(50) NOT NULL
);

-- Table for Book Shelves
CREATE TABLE book_shelves (
    shelf_id INT PRIMARY KEY AUTO_INCREMENT,
    shelf_number VARCHAR(20),
    section_id INT,
    FOREIGN KEY (section_id) REFERENCES library_sections(section_id)
);

-- Table for Availability Status
CREATE TABLE availability_status (
    status_id INT PRIMARY KEY AUTO_INCREMENT,
    status_name VARCHAR(20) NOT NULL
);

-- Table for Reviews and Ratings
CREATE TABLE book_reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT,
    user_id INT,
    review_text TEXT,
    rating INT,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Table for Library Events
CREATE TABLE library_events (
    event_id INT PRIMARY KEY AUTO_INCREMENT,
    event_name VARCHAR(100) NOT NULL,
    event_date DATE
);

-- Table for Financial Information
CREATE TABLE financial_information (
    financial_id INT PRIMARY KEY AUTO_INCREMENT,
    purchase_price DECIMAL(8, 2),
    budget_allocation DECIMAL(8, 2),
    revenue DECIMAL(8, 2)
);

-- Table for Cataloging Information
CREATE TABLE cataloging_information (
    catalog_id INT PRIMARY KEY AUTO_INCREMENT,
    dewey_decimal_classification VARCHAR(20),
    library_of_congress_classification VARCHAR(20)
);

-- Table for Digital Assets
CREATE TABLE digital_assets (
    asset_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT,
    asset_type VARCHAR(20),
    asset_url VARCHAR(255),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

-- Table for Security Information
CREATE TABLE security_information (
    security_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT,
    security_measure VARCHAR(255),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

-- Table for Rules and Policies
CREATE TABLE library_rules (
    rule_id INT PRIMARY KEY AUTO_INCREMENT,
    rule_text TEXT
);

-- Table for Integration with Online Platforms
CREATE TABLE online_platforms (
    platform_id INT PRIMARY KEY AUTO_INCREMENT,
    platform_name VARCHAR(50),
    platform_url VARCHAR(255)
);
