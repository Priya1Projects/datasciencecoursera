select name from salesperson s inner join  orders o on s.ID = o.salesperson_id
where o.Amount > 1300

select name from salesperson where ID in (select salesperson_id from orders where amount > 1300
)