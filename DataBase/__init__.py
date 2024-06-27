from .make_hash import make_hash_from_str,make_id_for_user

from .check_login_data import check_login_data_in_json,islogin_json,change_islogin_json,how_is_login_json,give_username_and_fullname
from .check_login_data import give_base_info_user,give_gender_islogin

from .log import find_last_id_json,add_log_json,change_one_value_in_json_data,find_index_from_id_json
from .log import delete_log_from_json_data,give_up_tabel_json_data_in_log
from .log import return_json_data_as_list,logout,true_false_value,test_true_false_value,clear_all_log

from .signup import SignUp

#Defind instance var
path_users_data = r"DataBase\users.json"
path_system_data = r"DataBase\system.json"
path_log_data = r"DataBase\log.json"