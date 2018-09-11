from app import db
from app.Models.Trip import Trip
from . import trip

from flask import render_template, redirect, url_for, flash, request, send_file
from flask_login import login_required, logout_user, login_user, current_user


import xlsxwriter


@trip.route('/')
@login_required
def index():
    logged_user = current_user
    return render_template('main/dashboard.html', title='Dashboard', user=logged_user)


@trip.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    logged_user = current_user
    if request.method == 'POST':
        req_data = request.form
        new_trip = Trip(tripid=req_data['tripID'],
                        from_=req_data['origin'],
                        to_=req_data['destination'],
                        vtype=req_data['vtype'],
                        ttype=req_data['ttype'],
                        time=req_data['time'],
                        distance=req_data['distance'],
                        user_id=logged_user.id)

        new_trip.total = req_data['cost']

        db.session.add(new_trip)
        db.session.commit()
        flash('Issue has been reported', 'success')

    return render_template('main/add.html', title='Add Trip', user=logged_user)

@trip.route('/export')
@login_required
def export():
    workbook = xlsxwriter.Workbook('Trip_recalculations.xlsx')
    worksheet = workbook.add_worksheet()

    data = Trip.query.all()

    headings = ['TripID', "distance", "time", "vtype", "ttype", "total", "from", "to", "logged_by"]

    row = 0
    col = 0

    # Iterate over the data and write it out row by row.
    for header in headings:
        worksheet.write(row, col, header)
        col += 1

    row += 1

    for trip in data:
        worksheet.write(row, 0, trip.tripid)
        worksheet.write(row, 1, trip.distance)
        worksheet.write(row, 2, trip.time)
        worksheet.write(row, 3, trip.vehicle_type)
        worksheet.write(row, 4, trip.trip_type)
        worksheet.write(row, 5, trip.total)
        worksheet.write(row, 6, trip.from_)
        worksheet.write(row, 7, trip.to_)
        worksheet.write(row, 8, trip.user.name + "<{}>".format(trip.user.email))
        row += 1

    workbook.close()

    print(workbook.get_default_url_format())

    return send_file('../Trip_recalculations.xlsx', as_attachment=True)

