import os
import pytest


def run():
    pytest.main(['-s', '-v','--alluredir','./report/item_result','--clean-alluredir','--allure-no-capture'])

    os.system('allure generate ./report/item_result/ -o ./report/item_report_allure/ --clean')



if __name__ == '__main__':
    run()
