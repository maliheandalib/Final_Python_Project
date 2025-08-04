--save ADMIN
insert into admin
    (admin_id, name, family, username, password)
values
    (12, malihe, andalib, malihe123, 1234567 )


--search ADMIN
select
    (admin_id, name, family, username, password)
from admin
where admin_id = 1

select *
from admin
where username='malihe' and password='12345678'


--edit ADMIN
update admin set name='?', family='?', username='?', password='?'
where admin_id = ?

--delete ADMIN
delete from admin where admin_id='1'

