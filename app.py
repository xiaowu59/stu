from flask import Flask, request, jsonify
import user
import score
import course
import profile

app = Flask(__name__)

# ========== 第一部分 用户注册登录接口 ==========
@app.route("/user/register", methods=["POST"])
def api_register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"code": 400, "msg": "用户名和密码不能为空"}), 400
    success, msg = user.register_user(username, password)
    if success:
        return jsonify({"code": 200, "msg": msg})
    else:
        return jsonify({"code": 400, "msg": msg}), 400

@app.route("/user/login", methods=["POST"])
def api_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"code": 400, "msg": "用户名和密码不能为空"}), 400
    success, result = user.login_user(username, password)
    if success:
        return jsonify({"code": 200, "msg": "登录成功", "user_id": result})
    else:
        return jsonify({"code": 400, "msg": result}), 400

# ========== 第二部分 成绩管理接口 ==========
@app.route("/score/add", methods=["POST"])
def api_add_score():
    data = request.get_json()
    user_id = data.get("user_id")
    course_id = data.get("course_id")
    score_val = data.get("score")
    if not user_id or not course_id or score_val is None:
        return jsonify({"code": 400, "msg": "参数不全"}), 400
    success, msg = score.add_score(user_id, course_id, score_val)
    if success:
        return jsonify({"code": 200, "msg": msg})
    else:
        return jsonify({"code": 400, "msg": msg}), 400

@app.route("/score/user/<int:user_id>", methods=["GET"])
def api_user_scores(user_id):
    res = score.get_scores_by_user(user_id)
    return jsonify({"code": 200, "data": res})

@app.route("/score/update/<int:sid>", methods=["PUT"])
def api_update_score(sid):
    data = request.get_json()
    new_sc = data.get("score")
    success, msg = score.update_score(sid, new_sc)
    if success:
        return jsonify({"code": 200, "msg": msg})
    return jsonify({"code": 400, "msg": msg}), 400

@app.route("/score/del/<int:sid>", methods=["DELETE"])
def api_del_score(sid):
    score.delete_score(sid)
    return jsonify({"code": 200, "msg": "成绩删除成功"})

# ========== 第三部分 课程管理接口 ==========
@app.route("/course/add", methods=["POST"])
def api_add_course():
    data = request.get_json()
    name = data.get("course_name")
    teacher = data.get("teacher")
    credit = data.get("credit")
    if not all([name, teacher, credit]):
        return jsonify({"code": 400, "msg":"参数不全"}),400
    success, msg = course.add_course(name, teacher, credit)
    return jsonify({"code": 200, "msg": msg})

@app.route("/course/list", methods=["GET"])
def api_course_list():
    return jsonify({"code": 200, "data": course.get_all_course()})

@app.route("/course/get/<int:cid>", methods=["GET"])
def api_get_course(cid):
    res = course.get_course_by_id(cid)
    if res:
        return jsonify({"code": 200, "data": res})
    return jsonify({"code": 404, "msg":"课程不存在"}),404

@app.route("/course/update/<int:cid>", methods=["PUT"])
def api_update_course(cid):
    data = request.get_json()
    name = data.get("course_name")
    teacher = data.get("teacher")
    credit = data.get("credit")
    ok = course.update_course(cid, name, teacher, credit)
    if ok:
        return jsonify({"code": 200, "msg":"修改成功"})
    return jsonify({"code": 400, "msg":"修改失败"}),400

@app.route("/course/del/<int:cid>", methods=["DELETE"])
def api_del_course(cid):
    course.delete_course(cid)
    return jsonify({"code": 200, "msg":"删除成功"})

# ========== 第四部分 个人中心接口 ==========
@app.route("/profile/info/<int:uid>", methods=["GET"])
def get_personal_info(uid):
    info = profile.get_user_basic_info(uid)
    if info:
        return jsonify({
            "code": 200,
            "msg": "查询成功",
            "data": info
        })
    return jsonify({
        "code": 404,
        "msg": "未找到该用户信息"
    }), 404

@app.route("/profile/updatepwd", methods=["POST"])
def update_user_pwd():
    req_data = request.get_json()
    uid = req_data.get("user_id")
    old_pwd = req_data.get("old_password")
    new_pwd = req_data.get("new_password")

    if not uid or not old_pwd or not new_pwd:
        return jsonify({
            "code": 400,
            "msg": "参数不能为空，请补齐信息"
        }), 400

    flag, tip = profile.change_password(uid, old_pwd, new_pwd)
    if flag:
        return jsonify({
            "code": 200,
            "msg": tip
        })
    else:
        return jsonify({
            "code": 400,
            "msg": tip
        }), 400

@app.route("/profile/stat/<int:uid>", methods=["GET"])
def get_user_stat(uid):
    stat_data = profile.get_personal_statistics(uid)
    return jsonify({
        "code": 200,
        "msg": "统计数据获取成功",
        "data": stat_data
    })

if __name__ == "__main__":
    app.run(debug=True)