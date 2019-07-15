@app.route("/api/me",methods=['GET','POST'])





def me():
    cont=request.json
    login=cont["login"]
    password=cont["password"]
    conn=sqlite3.connect("Pidory.db")
    cursor=conn.cursor()
    if(login in session):
        cursor.execute("select * from Pidory where username=?", (login,))
        resultatik=cursor.fetchall()
        result = {'id: ': resultatik[0][0],'username: ' : resultatik[0][1],'password: ' : resultatik[0][2]}
        return make_response(jsonify(result), 200)
    else:
        abort(403)



    return "Register"