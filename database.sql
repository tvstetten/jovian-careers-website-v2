-- MYSQL

use joviancareer;

create table
    jobs (
        id int NOT NULL AUTO_INCREMENT,
        title VARCHAR(250) NOT NULL,
        location VARCHAR(250) NOT NULL,
        salery INT,
        currency VARCHAR(10),
        responsabylities VARCHAR(2000),
        requirements VARCHAR(2000),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        PRIMARY KEY (id)
    );

CREATE TABLE
    applications (
        id INT NOT NULL AUTO_INCREMENT,
        job_id INT NOT NULL,
        full_name VARCHAR(250) NOT NULL,
        email VARCHAR(250) NOT NULL,
        linkedin_url VARCHAR(500),
        education VARCHAR(2000),
        work_experience VARCHAR(2000),
        resume_url VARCHAR(500),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        PRIMARY KEY (id)
    );