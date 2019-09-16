id=$(docker ps \
               | grep "mysql" \
               | awk '{print $1}') ; 
docker kill $id
