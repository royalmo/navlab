# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<Task %r>' % self.id

# @app.route('/', methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         task_content = request.form['content']
#         new_task = Todo(content=task_content)

#         db.session.add(new_task)
#         db.session.commit()
#         return redirect('/')

#     else:
#         tasks = Todo.query.order_by(Todo.date_created).all()
#         return render_template('pages/login.html.j2', tasks=tasks)


# @app.route('/delete/<int:id>')
# def delete(id):
#     task_to_delete = Todo.query.get_or_404(id)

#     db.session.delete(task_to_delete)
#     db.session.commit()
#     return redirect('/')

# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     task = Todo.query.get_or_404(id)

#     if request.method == 'POST':
#         task.content = request.form['content']
#         db.session.commit()
#         return redirect('/')

#     else:
#         return render_template('base/logged_in.html.j2', task=task)