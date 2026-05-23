# app.py 主入口
from flask import Flask, request, jsonify
import user
import score
import course

app = Flask(__name__)

# ---------- 原有登录注册、成绩接口保留 ----------

# ========== 新增第三部分：课程接口 ==========
# 新增课程
@app.route("/course/add", methods=["POST"])
def api_add_course():
    data = request.get_json()
    name = data.get("course_name")
    teacher = data.get("teacher")
    credit = data.get("credit")
    if not all([name, teacher, credit]):
        return jsonify({"msg":"参数不全"}),400
    course.add_course(name, teacher, credit)
    return jsonify({"msg":"课程添加成功"})

# 查询全部课程
@app.route("/course/list", methods=["GET"])
def api_course_list():
    return jsonify(course.get_all_course())

# 根据ID查询课程
@app.route("/course/get/<int:cid>", methods=["GET"])
def api_get_course(cid):
    res = course.get_course_by_id(cid)
    if res:
        return jsonify(res)
    return jsonify({"msg":"课程不存在"}),404

# 修改课程
@app.route("/course/update/<int:cid>", methods=["PUT"])
def api_update_course(cid):
    data = request.get_json()
    name = data.get("course_name")
    teacher = data.get("teacher")
    credit = data.get("credit")
    ok = course.update_course(cid, name, teacher, credit)
    if ok:
        return jsonify({"msg":"修改成功"})
    return jsonify({"msg":"修改失败"}),400

# 删除课程
@app.route("/course/del/<int:cid>", methods=["DELETE"])
def api_del_course(cid):
    course.delete_course(cid)
    return jsonify({"msg":"删除成功"})

if __name__ == "__main__":
    app.run(debug=True)