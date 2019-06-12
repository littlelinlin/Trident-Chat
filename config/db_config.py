# coding: utf-8
# @author  : lin
# @time    : 2019/6/3

import redis


# redis配置
redis_config = {
    'redis_db': 15,
    # 'redis_host': 'redis',
    'redis_host': '127.0.0.1',
    'redis_port': 6379,
    'redis_password': None
}

# mysql配置
mysql_config = {
    'db_name': 'TridentChat',
    'db_user': 'chat_user',
    'db_password': '111222',
    'db_port': 3306,
    'db_host': '39.106.53.169'
}

pool = redis.ConnectionPool(host=redis_config['redis_host'], port=redis_config['redis_port'],
                            db=redis_config['redis_db'])
redis_client = redis.Redis(connection_pool=pool)
