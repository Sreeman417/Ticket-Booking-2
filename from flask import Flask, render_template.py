from flask import Flask, render_template, request, redirect, url_for
_name_="_main_"
app = Flask(_name_)

# Sample data (could be replaced with a database)
available_tickets = 100
bookings = []

@app.route('/')
def index():
    return render_template('index.html', tickets=available_tickets)

@app.route('/book', methods=['GET', 'POST'])
def book_ticket():
    global available_tickets
    if request.method == 'POST':
        name = request.form['name']
        tickets_requested = int(request.form['tickets'])
        
        if tickets_requested <= available_tickets:
            bookings.append({'name': name, 'tickets': tickets_requested})
            available_tickets -= tickets_requested
            return redirect(url_for('confirmation', name=name, tickets=tickets_requested))
        else:
            return "Not enough tickets available. Try booking fewer tickets."
    return render_template('book.html')

@app.route('/confirmation')
def confirmation():
    name = request.args.get('name')
    tickets = request.args.get('tickets')
    return render_template('confirmation.html', name=name, tickets=tickets)

if _name_ == '_main_':
    app.run(debug=True)