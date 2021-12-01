DELIMITER $$
CREATE TRIGGER UserTrigger

    BEFORE INSERT ON User
        FOR EACH ROW
    BEGIN
    
        SET @usrCount = (SELECT COUNT(*)
                      FROM User
                      WHERE email = new.email);

        IF (@usrCount) > 0 THEN
            SIGNAL SQLSTATE '02000' 
            SET MESSAGE_TEXT = "Duplicate Email";
        END IF;
    end$$
delimiter ;
