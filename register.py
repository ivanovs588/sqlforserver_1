@app.route("/api/register",methods=['GET','POST'])





def register():
    cont=request.json
    login=cont["login"]
    password=cont["password"]
    conn=sqlite3.connect("Pidory.db")
    cursor=conn.cursor()
    cursor.execute("select id from Pidory where username=?",(login,))
    if len(cursor.fetchall())!=0:
        abort(402)
    else:
        cursor.execute("insert into Pidory (username,password) values(?,?)",(login,password))
        result = {'ok': 'ko'}
        return make_response(jsonify(result), 201)
        
        
        
        
        
        


    return "Register"