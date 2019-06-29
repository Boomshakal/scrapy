# salary_start, salary_end = '6千-8千'.split('-')
# print(salary_end.replace('千','000'))

#
# a = "{'tel': '***', 'sex': '2', 'label_name': '动画设计', 'head_pic_path': '', 'name': '肖女士', 'address': '杭州', 'work_years': '2', 'education': [{'code': '6', 'name': '本科'}], 'work_path': '', 'introduce': '', 'education_experience': [{'educationDate': '2013.09-2017.07', 'endDate': '1498867200000', 'levelKey': '本科', 'majorName': '动画', 'schoolName': '浙江工商大学', 'startDate': '1377993600000'}], 'project_experience': '', 'work_experience': [{'companyName': '浙江智邸文化传媒有限公司', 'desc': '节假日海报绘制 海报主图绘制', 'endDate': '0', 'jobTile': '插画师', 'jobTypeKey': 0, 'jobTypeName': '销售总监', 'startDate': '2019-03-01', 'workSalaryRange': '4001-6000元/月'}, {'companyName': '杭州墨宇文化创意有限公司', 'desc': '', 'endDate': '2018-12-01', 'jobTile': '插画师', 'jobTypeKey': 0, 'jobTypeName': '销售总监', 'startDate': '2017-12-01', 'workSalaryRange': '4001-6000元/月'}, {'companyName': '杭州棕象文化有限公司', 'desc': '', 'endDate': '2017-12-01', 'jobTile': '导演助理 插画', 'jobTypeKey': 0, 'jobTypeName': '销售总监', 'startDate': '2017-06-01', 'workSalaryRange': '4001-6000元/月'}], 'salary_start': 6000, 'salary_end': 8000, 'for_id': 674981737, 'other_info': ''}".replace('\'','\"')
# print(a)
# import json
#
# def dict_to_json():
#     dict = {}
#     dict['name'] = 'many'
#     dict['age'] = 10
#     dict['sex'] = 'male'
#     print(dict)  # 输出：{'name': 'many', 'age': 10, 'sex': 'male'}
#     j = json.dumps(dict)
#     print(j)  # 输出：{"name": "many", "age": 10, "sex": "male"}
#
#
# if __name__ == '__main__':
#     dict_to_json()
# salary_start = '2万'
# if salary_start.endswith('千'):
#     salary_start = int(salary_start[:-1]) * 1000
# elif salary_start.endswith('万'):
#     salary_start = int(salary_start[:-1]) * 10000
# print(salary_start)

import time
print(time.localtime(time.time()))
