SELECT count(*) as USERS
from USER_INFO
where DATE_FORMAT(JOINED, '%Y') = '2021'
  and AGE BETWEEN 20 and 29;