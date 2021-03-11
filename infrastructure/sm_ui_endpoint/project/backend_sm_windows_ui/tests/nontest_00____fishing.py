import uuid
import random

from navigation import Navigation
import api_approve_ui


# api test - users ui - create new user
def test():

    nav = Navigation()
    nav.start()
    nav.setup_controls_and_dialogs()

    print('\ntest start\n')

#    nav.control('home', 'menu').click()
#    nav.control('menu', 'methods').click()
#    nav.control('methods', 'menu').click()
#    nav.control('menu', 'home').click()
#    nav.control('home', 'menu').click()
#    nav.control('menu', 'methods').click()
#    nav.control('methods', 'home').click()
#    nav.control('home', 'approve').click()
#    nav.control('approve', 'home').click()

#    nav.control('home', 'menu').click()
#    nav.control('menu', 'home').click()
    nav.control('home', 'menu').click()

    print('----4----')
    # nav.fish(5)

    nav.control('menu', 'user_roles').click()

    
    # nav.control('menu', 'user').click()
    nav.fish(6)
    # nav.control('menu', 'user').click()
    assert False, "done"

    print('test is done')





    y = api_users_ui.get_users_list(nav)
    print('there are {} users'.format(len(y)))

    the_key = None
    for [key, value] in y.items():
        print('{} {}'.format(key, value))
        if value != "":
            the_key = key

