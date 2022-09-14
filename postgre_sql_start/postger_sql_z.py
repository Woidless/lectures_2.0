''' Task 1
Найдите 10 самых часто встречающихся слов из таблицы wordform. Ожидаемый вывод:
plaintext    
-----------   
the    
and    
i    
to    
of    
a    
you    
...   
(10 rows)
'''
# SELECT plaintext FROM wordform ORDER BY wordformid FETCH FIRST 10 ROW ONLY;
# SELECT plaintext FROM wordform ORDER BY occurences DESC LIMIT(10);
# SELECT plaintext FROM wordform LIMIT 10;

''' Task 2
Найдите все слова, которые начинаются с буквы a(таблица wordform),
регистр не должен иметь значения. Ожидаемый вывод:
plaintext       
-------------------   
and   
a   
as   
all   
are   
at   
am   
...  
(1569 rows) 
'''
# SELECT plaintext FROM wordform WHERE stemtext ILIKE 'a%';
# SELECT plaintext FROM wordform WHERE plaintext LIKE 'a%' OR plaintext LIKE 'A%';
# SELECT plaintext FROM wordform WHERE plaintext ILIKE 'a%';

'''Task 3
Выведите название всех произведений, которые относятся к жанру p(таблица work).
Ожидаемый вывод:
| title | genretype |
| Lover's Complaint      | p | 
--------------------------------
| Passionate Pilgrim     | p | 
--------------------------------
| Phoenix and the Turtle | p | 
--------------------------------
| Rape of Lucrece        | p | 
--------------------------------
| Venus and Adonis       | p | 
--------------------------------
(5 rows)
'''
# SELECT title, genretype FROM work WHERE genretype IN ('p');
# SELECT title, genretype FROM work WHERE genretype LIKE 'p';
# SELECT title, genretype FROM work WHERE genretype = 'p';

''' Task 4
Найдите среднее количество параграфов в произведениях жанра t (таблица work).
Ожидаемый вывод:
avg      
---------------------- 
1070.8181818181818182  
(1 row) 
'''
# SELECT AVG(totalparagraphs) AS avg FROM work WHERE genretype = 't' GROUP BY genretype;
# SELECT AVG(totalparagraphs) AS avg FROM work WHERE genretype LIKE 't';
# SELECT AVG(totalparagraphs) AS avg FROM work WHERE genretype = 't';

''' Task 5
Выведите названия всех произведений из таблицы work, в которых количество слов выше среднего.
Ожидаемый вывод:
title             
---------------------------   
All's Well That Ends Well   
Antony and Cleopatra   
As You Like It   
Coriolanus   
Cymbeline   
Hamlet   
Henry IV, Part I   
...  
(28 rows) 
'''
# SELECT title FROM work WHERE totalwords > (SELECT SUM(totalwords) FROM work) / (SELECT COUNT(*) FROM work);
# SELECT title FROM work WHERE totalwords > (SELECT AVG(totalwords) FROM work);



''' Task 6
Выведите имя героя, количество его реплик и название произведения,
в котором этот герой встречается(таблицы character_work и character).
Ожидаемый вывод:
   charname         | speechcount |     title            
--------------------+-------------+------------------------ 
First Apparition    |           1 | Macbeth 
First Citizen       |           3 | Romeo and Juliet 
First Conspirator   |           3 | Coriolanus 
First Gentleman     |           1 | Othello 
First Goth          |           4 | Titus Andronicus 
... 
(1346 row) 
'''
# SELECT c.charname, c.speechcount, w.title FROM character as c INNER JOIN character_work as cw ON c.charid = cw.charid INNER JOIN work as w ON cw.workid = w.workid;
# SELECT character.charname, character.speechcount, work.title FROM character JOIN character_work ON character_work.charid = character.charid JOIN work ON character_work.workid = work.workid;

'''Task 7
Выведите среднее количество реплик героев в произведении 'Romeo and Juliet'
(таблицы character_work и work).
Ожидаемый вывод:
round |      title          
-------+------------------      
   26 | Romeo and Juliet  
(1 row) 
'''
# SELECT ROUND(AVG(c.speechcount)), w.title FROM character c INNER JOIN character_work cw ON c.charid = cw.charid INNER JOIN work w ON cw.workid = w.workid GROUP BY title HAVING title LIKE 'Romeo and Juliet';
# SELECT ROUND(AVG(character.speechcount)), work.title FROM character JOIN character_work ON character.charid = character_work.charid JOIN work ON work.workid = character_work.workid GROUP BY title HAVING title = 'Romeo and Juliet';

'''Task 8
Выведите общее количество слов в каждой из секций в таблице paragraph. Ожидаемый вывод:
section |  sum     
---------+--------         
      0 |   2963         
      1 | 219622         
      3 | 174015         
      5 | 148638         
      4 | 168204        
      2 | 170774  
(6 rows) 
'''
# SELECT section, SUM(wordcount) FROM paragraph GROUP BY section;

'''Tassk 9
Выведите имя и количество реплик героев, у которых от 15 до 30 реплик (таблица character).
Ожидаемый вывод:
   charname    | speechcount   
----------------+-------------   
First Murderer |          21   
First Witch    |          23   
Second Witch   |          15   
Aegeon         |          17   
Aemilia        |          16   
Agrippa        |          28   
Alexas         |          15   
...  
(153 rows)
'''
# SELECT charname, speechcount FROM character WHERE speechcount >= 15 AND speechcount <= 30;
# SELECT charname, speechcount FROM character WHERE speechcount IN (SELECT * FROM GENERATE_SERIES(15, 30));
# SELECT charname, speechcount FROM character WHERE speechcount BETWEEN 15 AND 30;

'''Task 10
Выведите название и год написания всех произведений, которые были написаны в 17 веке (таблица work).
Ожидаемый вывод:
          title           | year   
---------------------------+------   
All's Well That Ends Well | 1602   
Antony and Cleopatra      | 1606   
Coriolanus                | 1607   
Cymbeline                 | 1609   
Henry VIII                | 1612   
King Lear                 | 1605   
Lover's Complaint         | 1609   
...  
(17 rows) 
'''
# SELECT title, year FROM work WHERE year >= 1601 AND year <= 1700;
# SELECT title, year FROM work WHERE year BETWEEN 1601 AND 1700;
# SELECT title, year FROM work WHERE year IN (SELECT * FROM GENERATE_SERIES(1601, 1700));

'''task 11
Выведите полные названия всех произведений, которые имеют в полном названии слово the (таблица work).
Поиск должен быть чувствителен к регистру(только для the с маленькими буквами). Ожидаемый вывод:
longtitle                  
----------------------------------------   
The Tragedy of Othello, Moor of Venice   
The Phoenix and the Turtle   
The Taming of the Shrew   
The Tragedy of Timon of Athens  
(4 rows) 
'''
# SELECT longtitle FROM work WHERE longtitle LIKE '%the%';
# SELECT longtitle FROM work WHERE longtitle ~ 'the';

'''Task 12
Выведите все уникальные секции в paragraph. Ожидаемый вывод:
section   
---------         
0         
1         
3         
5         
4         
2  
(6 rows) 
'''
# SELECT DISTINCT section FROM paragraph;
# SELECT section FROM paragraph GROUP BY section;

'''Task 13
Для каждой главы выведите: chapterid, описание и название произведения,
к которой относится данная глава (таблицы chapter и work). Ожидаемый вывод:
chapterid |      description      |   title     
-----------+-----------------------+--------------   
    18934 | Prologue.             | Henry V       
    18704 | DUKE ORSINO's palace. | Twelfth Night       
    18705 | The sea-coast.        | Twelfth Night       
    18706 | OLIVIA'S house.       | Twelfth Night       
    18707 | DUKE ORSINO's palace. | Twelfth Night       
    18708 | OLIVIA'S house.       | Twelfth Night       
    18709 | The sea-coast.        | Twelfth Night   
...  
(945 rows) 
'''
# SELECT c.chapterid, c.description, w.title FROM chapter AS c INNER JOIN work AS w ON c.workid = w.workid;
# SELECT c.chapterid, c.description, w.title FROM chapter c FULL JOIN work w ON c.workid = w.workid;
# SELECT chapter.chapterid, chapter.description, work.title FROM chapter JOIN work ON chapter.workid = work.workid;

'''Task 14
Для каждого параграфа выведите: номер параграфа, имя героя, и количество реплик героя
(таблицы paragraph и character). Ожидаемый вывод:
paragraphnum |      charname      | speechcount   
--------------+------------------- +-------------              
           3 | (stage directions) |         126              
           4 | Orsino             |          59             
          19 | Curio              |           4             
          20 | Orsino             |          59             
          21 | Curio              |           4             
          22 | Orsino             |          59             
          30 | Valentine          |           3   
...  
(35465 rows) 
'''
# SELECT paragraph.paragraphnum, character.charname, character.speechcount FROM paragraph JOIN character ON character.charid = paragraph.charid;
# SELECT p.paragraphnum, c.charname, c.speechcount FROM paragraph AS p INNER JOIN character AS c ON c.charid = p.charid;

'''Task 15
Для каждого параграфа выведите: номер параграфа, название произведения и год выхода этого произведения
(таблицы paragraph и work). Ожидаемый вывод:
paragraphnum |           title           | year   
--------------+---------------------------+-----              
           3 | Twelfth Night             | 1599              
           4 | Twelfth Night             | 1599             
          19 | Twelfth Night             | 1599             
          20 | Twelfth Night             | 1599             
          21 | Twelfth Night             | 1599             
          22 | Twelfth Night             | 1599             
          30 | Twelfth Night             | 1599   
...  
(35465 rows) 
'''
# SELECT paragraph.paragraphnum, work.title, work.year FROM paragraph JOIN work ON paragraph.workid = work.workid;
# SELECT p.paragraphnum, w.title, w.year FROM paragraph p INNER JOIN work w ON p.workid = w.workid;
