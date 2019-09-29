# Start docker container
docker run -d --name some-mysql \
           --rm \
           -p 3306:3306 \
           -e MYSQL_ROOT_PASSWORD=my-secret-root-pw \
           -e MYSQL_USER=chr \
           -e MYSQL_PASSWORD=my-secret-pw \
            mysql

# Give the database some time to come up
mysqladmin --user=root --password=my-secret-root-pw \
           --host='127.0.0.1'  \
            --silent status

while [ $? == 1  ]
do
  sleep 5
  mysqladmin --user=root --password=my-secret-root-pw \
             --host='127.0.0.1'  \
             --silent status
done

# Create database books and grant rights to user chr
mysqladmin --user=root \
           --password=my-secret-root-pw \
            --host='127.0.0.1'  create books
echo 'grant all on books.* to 'chr';' \
              | mysql --user=root \
                      --password=my-secret-root-pw \
                      --host='127.0.0.1' books
