--write code to run all sql files in folder
FOR file IN *.sql WHERE file != 'run.sql' DO
    \i :file
END LOOP;
