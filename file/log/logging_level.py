import logging


if __name__ == '__main__':

    logger = logging.getLogger('main') #Logger 선언
    logging.basicConfig(level = logging.DEBUG)
    logger.setLevel(logging.INFO)

    steam_handler = logging.FileHandler(
        'my.log',mode = 'w',encoding='utf8'
    )
    logger.addHandler(steam_handler)


    logging.debug('틀렸어!!')
    logging.info('확인해')
    logging.warning('조심해!!')
    logging.error('에러났어!!')
    logging.critical('망했어!!') 
#이 파이썬 파일을 실행하면 warning부터 나온다. 이유는 기본 logging level 설정이 warning으로 되어 있기 때문