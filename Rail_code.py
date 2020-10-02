#----------------------------------------------------------------------------------------------------------------
#initial setup
#----------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
import sqlite3

#defining raise frame func
def raise_frame(frame):
    frame.tkraise()

connection = sqlite3.connect("Rail_database.db")
crsr = connection.cursor()

#root frame
root = Tk()
root.state('zoomed')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

#setting the minimum frame size
root.geometry("1600x500")

def go_home():
	raise_frame(frame_dashboard)

def reset_data():
	crsr.execute("UPDATE data SET A_S = 2, W_L = 1")
	crsr.execute("DELETE from tickets")
	crsr.execute("DELETE from sqlite_sequence")
	#MyTickets_Click()
	connection.commit()

def log_out():
	raise_frame(frame_login)
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
#setting up the frames
#----------------------------------------------------------------------------------------------------------------
frame_register = Frame(root)
frame_login = Frame(root)
frame_dashboard = Frame(root)
frame_fill = Frame(root)
frame_pay = Frame(root)
frame_show = Frame(root)
frame_cancellation = Frame(root)
frame_tickets = Frame(root)
frame_complaint = Frame(root)
frame_cancellation_cnf = Frame(root)
frame_active_tickets = Frame(root)
frame_inactive_tickets = Frame(root)


#setting values for each frame
for frame in (frame_login, frame_dashboard, frame_register, frame_fill, frame_pay, frame_show, frame_cancellation, frame_tickets, frame_complaint, frame_cancellation_cnf, frame_active_tickets, frame_inactive_tickets):
	frame.grid(row=0, column=0, sticky="news")
	frame.config(highlightbackground="black", highlightthickness=1, height=500, width=1240)
	frame.grid_propagate(False)
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
#frame register setup
#----------------------------------------------------------------------------------------------------------------
Label(frame_register, text="             ").pack()
Label(frame_register, text="             ").pack()
Label(frame_register, text="             ").pack()
Label(frame_register, text="             ").pack()
Label(frame_register, text="             ").pack()
Label(frame_register, text="             ").pack()
Label(frame_register, text="             ").pack()
Label(frame_register, text="             ").pack()
Label(frame_register, text="             ").pack()
Label(frame_register, text="             ").pack()
Label(frame_register, text="             ").pack()
Label(frame_register, text="             ").pack()
user_name_reg_entry = Entry(frame_register, width=20, justify="center")
user_name_reg_entry.insert(0, "Enter username")
user_name_reg_entry.pack()

password_reg_entry = Entry(frame_register, width=20, justify="center")
password_reg_entry.insert(0, "Enter Password")
password_reg_entry.pack()

reg_cnf_btn = Button(frame_register, text="Submit")
reg_cnf_btn.pack()
Button(frame_register, text="go back", command=log_out).pack()
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
#frame dashboard setup
#----------------------------------------------------------------------------------------------------------------
Label(frame_dashboard, text="             ").pack()
Label(frame_dashboard, text="             ").pack()
label_main = Label(frame_dashboard)
label_main.config(font=("Courier", 44))
label_main.pack()

label2 = Label(frame_dashboard, text="Welcome to our Railway system!!")
label2.config(font=("Courier", 12))
label2.pack()

label3 = Label(frame_dashboard, text="Select the below services.")
label3.config(font=("Courier", 12))
label3.pack()

Label(frame_dashboard, text="             ").pack()

book_btn = Button(frame_dashboard, text="Book")
book_btn.pack()

Label(frame_dashboard, text="             ").pack()

cancel_btn = Button(frame_dashboard, text="cancellation")
cancel_btn.pack()

Label(frame_dashboard, text="             ").pack()

tickets_btn = Button(frame_dashboard, text="My Tickets")
tickets_btn.pack()

Label(frame_dashboard, text="             ").pack()

complaint_btn = Button(frame_dashboard, text="Complaint")
complaint_btn.pack()

Label(frame_dashboard, text="             ").pack()

reset_data_btn = Button(frame_dashboard, text="reset the availability", command=reset_data)
reset_data_btn.pack()

Label(frame_dashboard, text="             ").pack()

Button(frame_dashboard, text="Logout", command=log_out).pack()

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
#frame fill setup
#----------------------------------------------------------------------------------------------------------------
Label(frame_fill, text="             ").pack()
Label(frame_fill, text="             ").pack()
label_fill_main = Label(frame_fill, text="Fill the passenger details")
label_fill_main.config(font=("Courier", 44))
label_fill_main.pack()
Label(frame_fill, text="             ").pack()
Label(frame_fill, text="             ").pack()
Label(frame_fill, text="             ").pack()
Label(frame_fill, text="             ").pack()
booking_status = Label(frame_fill)
passenger_name_entry = Entry(frame_fill, width=20, justify="center")
age_entry = Entry(frame_fill, width=20, justify="center")
gender_entry = Entry(frame_fill, width=20, justify="center")
aadhar_no_entry = Entry(frame_fill, width=20, justify="center")
phone_no_entry = Entry(frame_fill, width=20, justify="center")
travel_date_entry = Entry(frame_fill, width=20, justify="center")

passenger_name_entry.insert(0, "passenger name")
age_entry.insert(0, "age")
gender_entry.insert(0, "gender")
aadhar_no_entry.insert(0, "aadhar no")
phone_no_entry.insert(0, "phone no")
travel_date_entry.insert(0, "travel date")

#placing them
booking_status.pack()
Label(frame_fill, text="             ").pack()
passenger_name_entry.pack()
Label(frame_fill, text="             ").pack()
age_entry.pack()
Label(frame_fill, text="             ").pack()
gender_entry.pack()
Label(frame_fill, text="             ").pack()
aadhar_no_entry.pack()
Label(frame_fill, text="             ").pack()
phone_no_entry.pack()
Label(frame_fill, text="             ").pack()
travel_date_entry.pack()
Label(frame_fill, text="             ").pack()
Label(frame_fill, text="             ").pack()

#go to payment btn
pay_btn = Button(frame_fill, text="Go to payment options.")
pay_btn.pack()
Label(frame_fill, text="             ").pack()
#placing the home button
Button(frame_fill, text="go home", command=go_home).pack()
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
#frame pay setup
#----------------------------------------------------------------------------------------------------------------
Label(frame_pay, text="             ").pack()
Label(frame_pay, text="             ").pack()
Label(frame_pay, text="             ").pack()
Label(frame_pay, text="             ").pack()
Label(frame_pay, text="             ").pack()
Label(frame_pay, text="             ").pack()
Label(frame_pay, text="             ").pack()
Label(frame_pay, text="             ").pack()
Label(frame_pay, text="             ").pack()
Label(frame_pay, text="             ").pack()
Label(frame_pay, text="             ").pack()

Label(frame_pay, text="Enter the Card Details below to confirm your ticket", font=("Courier", 30)).pack()
Label(frame_pay, text="             ").pack()
Label(frame_pay, text="             ").pack()

#taking payment info
card_no = Entry(frame_pay, width=20, justify="center")
exp_date = Entry(frame_pay, width=20, justify="center")
cvv = Entry(frame_pay, width=20, justify="center")

#placeholder
card_no.insert(0,"enter the card no")
exp_date.insert(0, "Enter the exp date")
cvv.insert(0, "Enter the cvv no")

#positioning
card_no.pack()
Label(frame_pay, text="             ").pack()
exp_date.pack()
Label(frame_pay, text="             ").pack()
cvv.pack()
Label(frame_pay, text="             ").pack()

#pay conf btn
pay_cnf_btn = Button(frame_pay, text="Pay")
pay_cnf_btn.pack()

Label(frame_pay, text="             ").pack()

Button(frame_pay, text="go home", command=go_home).pack()
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
#frame show setup
#----------------------------------------------------------------------------------------------------------------
Label(frame_show, text="             ").pack()
Label(frame_show, text="             ").pack()
Label(frame_show, text="             ").pack()
Label(frame_show, text="             ").pack()
show_label = Label(frame_show)
show_label.pack()
Button(frame_show, text="go home", command=go_home).pack()
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
#frame cancellation setup
#----------------------------------------------------------------------------------------------------------------
Label(frame_cancellation, text="                        ").pack()
Label(frame_cancellation, text="                        ").pack()
Label(frame_cancellation, text="                        ").pack()
Label(frame_cancellation, text="Your previous bookings :", font=("Courier", 30)).pack()
Label(frame_cancellation, text="                        ").grid(row=0, column=0)
Label(frame_cancellation, text="                        ").grid(row=1, column=0)
Label(frame_cancellation, text="                        ").grid(row=2, column=0)
Label(frame_cancellation, text="                        ").grid(row=3, column=0)
Label(frame_cancellation, text="                        ").grid(row=4, column=0)
Label(frame_cancellation, text="                        ").grid(row=5, column=0)
Label(frame_cancellation, text="                        ").grid(row=6, column=0)
Label(frame_cancellation, text="                        ").grid(row=7, column=0)
Label(frame_cancellation, text="                        ").grid(row=8, column=0)
Label(frame_cancellation, text="                        ").grid(row=10, column=0)
Label(frame_cancellation, text="                        ").grid(row=11, column=0)
Label(frame_cancellation, text="                        ").grid(row=12, column=0)
Label(frame_cancellation, text="                        ").grid(row=13, column=0)
Label(frame_cancellation, text="                        ").grid(row=14, column=0)
Label(frame_cancellation, text="                        ").grid(row=15, column=0)
Label(frame_cancellation, text="Ticket ID-NO", width=12, borderwidth=2, relief="groove").grid(row=16, column=1)
Label(frame_cancellation, text="Passenger Name",width=12, borderwidth=2, relief="groove").grid(row=16, column=2)
Label(frame_cancellation, text="Age",width=12, borderwidth=2, relief="groove").grid(row=16, column=3)
Label(frame_cancellation, text="Gender",width=12, borderwidth=2, relief="groove").grid(row=16, column=4)
Label(frame_cancellation, text="Aadhar No",width=12, borderwidth=2, relief="groove").grid(row=16, column=5)
Label(frame_cancellation, text="Phone No",width=12, borderwidth=2, relief="groove").grid(row=16, column=6)
Label(frame_cancellation, text="Travel Date",width=12, borderwidth=2, relief="groove").grid(row=16, column=7)
Label(frame_cancellation, text="Train No",width=12, borderwidth=2, relief="groove").grid(row=16, column=8)
Label(frame_cancellation, text="Source Stn",width=12, borderwidth=2, relief="groove").grid(row=16, column=9)
Label(frame_cancellation, text="Destination Stn",width=12, borderwidth=2, relief="groove").grid(row=16, column=10)
Label(frame_cancellation, text="Activity",width=12, borderwidth=2, relief="groove").grid(row=16, column=11)
Label(frame_cancellation, text="Status",width=12, borderwidth=2, relief="groove").grid(row=16, column=12)

Label(frame_cancellation, text="                        ").pack(side="bottom")
Label(frame_cancellation, text="                        ").pack(side="bottom")
Label(frame_cancellation, text="                        ").pack(side="bottom")
Label(frame_cancellation, text="                        ").pack(side="bottom")
Label(frame_cancellation, text="                        ").pack(side="bottom")
Label(frame_cancellation, text="                        ").pack(side="bottom")
Label(frame_cancellation, text="                        ").pack(side="bottom")
Label(frame_cancellation, text="                        ").pack(side="bottom")
Label(frame_cancellation, text="                        ").pack(side="bottom")
Label(frame_cancellation, text="                        ").pack(side="bottom")


cancel_entry = Entry(frame_cancellation, width=10, justify="center")
cancel_entry.insert(0, "ticket id")
cancel_cnf_btn = Button(frame_cancellation, text="Confirm Cancel")
Button(frame_cancellation, text="go home", command=go_home).pack(side="bottom")
Label(frame_cancellation, text="                        ").pack(side="bottom")
cancel_cnf_btn.pack(side="bottom")
Label(frame_cancellation, text="                        ").pack(side="bottom")
cancel_entry.pack(side="bottom")
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
#frame active  tickets setup
#----------------------------------------------------------------------------------------------------------------

active_ticket_btn = Button(frame_tickets, text="Active Tickets")
inactive_ticket_btn = Button(frame_tickets, text="Inactive Tickets")
active_ticket_btn.pack(side="left", fill="both", expand="true")
inactive_ticket_btn.pack(side="left", fill="both", expand="true")
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
#frame active  tickets setup
#----------------------------------------------------------------------------------------------------------------
Label(frame_active_tickets, text="                        ").pack()
Label(frame_active_tickets, text="                        ").pack()
Label(frame_active_tickets, text="                        ").pack()
Label(frame_active_tickets, text="Your previous bookings :", font=("Courier", 30)).pack()
Label(frame_active_tickets, text="                        ").grid(row=0, column=0)
Label(frame_active_tickets, text="                        ").grid(row=1, column=0)
Label(frame_active_tickets, text="                        ").grid(row=2, column=0)
Label(frame_active_tickets, text="                        ").grid(row=3, column=0)
Label(frame_active_tickets, text="                        ").grid(row=4, column=0)
Label(frame_active_tickets, text="                        ").grid(row=5, column=0)
Label(frame_active_tickets, text="                        ").grid(row=6, column=0)
Label(frame_active_tickets, text="                        ").grid(row=7, column=0)
Label(frame_active_tickets, text="                        ").grid(row=8, column=0)
Label(frame_active_tickets, text="                        ").grid(row=10, column=0)
Label(frame_active_tickets, text="                        ").grid(row=11, column=0)
Label(frame_active_tickets, text="                        ").grid(row=12, column=0)
Label(frame_active_tickets, text="                        ").grid(row=13, column=0)
Label(frame_active_tickets, text="                        ").grid(row=14, column=0)
Label(frame_active_tickets, text="                        ").grid(row=15, column=0)
Label(frame_active_tickets, text="Ticket ID-NO", width=12, borderwidth=2, relief="groove").grid(row=16, column=1)
Label(frame_active_tickets, text="Passenger Name",width=12, borderwidth=2, relief="groove").grid(row=16, column=2)
Label(frame_active_tickets, text="Age",width=12, borderwidth=2, relief="groove").grid(row=16, column=3)
Label(frame_active_tickets, text="Gender",width=12, borderwidth=2, relief="groove").grid(row=16, column=4)
Label(frame_active_tickets, text="Aadhar No",width=12, borderwidth=2, relief="groove").grid(row=16, column=5)
Label(frame_active_tickets, text="Phone No",width=12, borderwidth=2, relief="groove").grid(row=16, column=6)
Label(frame_active_tickets, text="Travel Date",width=12, borderwidth=2, relief="groove").grid(row=16, column=7)
Label(frame_active_tickets, text="Train No",width=12, borderwidth=2, relief="groove").grid(row=16, column=8)
Label(frame_active_tickets, text="Source Stn",width=12, borderwidth=2, relief="groove").grid(row=16, column=9)
Label(frame_active_tickets, text="Destination Stn",width=12, borderwidth=2, relief="groove").grid(row=16, column=10)
Label(frame_active_tickets, text="Activity",width=12, borderwidth=2, relief="groove").grid(row=16, column=11)
Label(frame_active_tickets, text="Status",width=12, borderwidth=2, relief="groove").grid(row=16, column=12)

Label(frame_active_tickets, text="                        ").pack(side="bottom")
Label(frame_active_tickets, text="                        ").pack(side="bottom")
Label(frame_active_tickets, text="                        ").pack(side="bottom")
Label(frame_active_tickets, text="                        ").pack(side="bottom")
Label(frame_active_tickets, text="                        ").pack(side="bottom")
Label(frame_active_tickets, text="                        ").pack(side="bottom")
Label(frame_active_tickets, text="                        ").pack(side="bottom")
Label(frame_active_tickets, text="                        ").pack(side="bottom")
Label(frame_active_tickets, text="                        ").pack(side="bottom")
Label(frame_active_tickets, text="                        ").pack(side="bottom")
Label(frame_active_tickets, text="                        ").pack(side="bottom")
Label(frame_active_tickets, text="                        ").pack(side="bottom")
Label(frame_active_tickets, text="                        ").pack(side="bottom")
Label(frame_active_tickets, text="                        ").pack(side="bottom")

Button(frame_active_tickets, text="go home", command=go_home).pack(side="bottom")
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
#frame inactive active  tickets setup
#----------------------------------------------------------------------------------------------------------------
Label(frame_inactive_tickets, text="                        ").pack()
Label(frame_inactive_tickets, text="                        ").pack()
Label(frame_inactive_tickets, text="                        ").pack()
Label(frame_inactive_tickets, text="Your previous bookings :", font=("Courier", 30)).pack()
Label(frame_inactive_tickets, text="                        ").grid(row=0, column=0)
Label(frame_inactive_tickets, text="                        ").grid(row=1, column=0)
Label(frame_inactive_tickets, text="                        ").grid(row=2, column=0)
Label(frame_inactive_tickets, text="                        ").grid(row=3, column=0)
Label(frame_inactive_tickets, text="                        ").grid(row=4, column=0)
Label(frame_inactive_tickets, text="                        ").grid(row=5, column=0)
Label(frame_inactive_tickets, text="                        ").grid(row=6, column=0)
Label(frame_inactive_tickets, text="                        ").grid(row=7, column=0)
Label(frame_inactive_tickets, text="                        ").grid(row=8, column=0)
Label(frame_inactive_tickets, text="                        ").grid(row=10, column=0)
Label(frame_inactive_tickets, text="                        ").grid(row=11, column=0)
Label(frame_inactive_tickets, text="                        ").grid(row=12, column=0)
Label(frame_inactive_tickets, text="                        ").grid(row=13, column=0)
Label(frame_inactive_tickets, text="                        ").grid(row=14, column=0)
Label(frame_inactive_tickets, text="                        ").grid(row=15, column=0)
Label(frame_inactive_tickets, text="Ticket ID-NO", width=12, borderwidth=2, relief="groove").grid(row=16, column=1)
Label(frame_inactive_tickets, text="Passenger Name",width=12, borderwidth=2, relief="groove").grid(row=16, column=2)
Label(frame_inactive_tickets, text="Age",width=12, borderwidth=2, relief="groove").grid(row=16, column=3)
Label(frame_inactive_tickets, text="Gender",width=12, borderwidth=2, relief="groove").grid(row=16, column=4)
Label(frame_inactive_tickets, text="Aadhar No",width=12, borderwidth=2, relief="groove").grid(row=16, column=5)
Label(frame_inactive_tickets, text="Phone No",width=12, borderwidth=2, relief="groove").grid(row=16, column=6)
Label(frame_inactive_tickets, text="Travel Date",width=12, borderwidth=2, relief="groove").grid(row=16, column=7)
Label(frame_inactive_tickets, text="Train No",width=12, borderwidth=2, relief="groove").grid(row=16, column=8)
Label(frame_inactive_tickets, text="Source Stn",width=12, borderwidth=2, relief="groove").grid(row=16, column=9)
Label(frame_inactive_tickets, text="Destination Stn",width=12, borderwidth=2, relief="groove").grid(row=16, column=10)
Label(frame_inactive_tickets, text="Activity",width=12, borderwidth=2, relief="groove").grid(row=16, column=11)
Label(frame_inactive_tickets, text="Status",width=12, borderwidth=2, relief="groove").grid(row=16, column=12)

Label(frame_inactive_tickets, text="                        ").pack(side="bottom")
Label(frame_inactive_tickets, text="                        ").pack(side="bottom")
Label(frame_inactive_tickets, text="                        ").pack(side="bottom")
Label(frame_inactive_tickets, text="                        ").pack(side="bottom")
Label(frame_inactive_tickets, text="                        ").pack(side="bottom")
Label(frame_inactive_tickets, text="                        ").pack(side="bottom")
Label(frame_inactive_tickets, text="                        ").pack(side="bottom")
Label(frame_inactive_tickets, text="                        ").pack(side="bottom")
Label(frame_inactive_tickets, text="                        ").pack(side="bottom")
Label(frame_inactive_tickets, text="                        ").pack(side="bottom")
Label(frame_inactive_tickets, text="                        ").pack(side="bottom")
Label(frame_inactive_tickets, text="                        ").pack(side="bottom")
Label(frame_inactive_tickets, text="                        ").pack(side="bottom")
Label(frame_inactive_tickets, text="                        ").pack(side="bottom")

Button(frame_inactive_tickets, text="go home", command=go_home).pack(side="bottom")
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------
#frame complaint setup
#----------------------------------------------------------------------------------------------------------------
Label(frame_complaint, text="                        ").pack()
Label(frame_complaint, text="                        ").pack()
Label(frame_complaint, text="                        ").pack()
Label(frame_complaint, text="                        ").pack()
Label(frame_complaint, text="                        ").pack()
Label(frame_complaint, text="                        ").pack()
complaint_text = Text(frame_complaint, width=50, height=20)
complaint_text.pack()
Label(frame_complaint, text="                        ").pack()
Label(frame_complaint, text="                        ").pack()
complaint_cnf_btn = Button(frame_complaint, text="Submit")
complaint_cnf_btn.pack()
Label(frame_complaint, text="                        ").pack()
Button(frame_complaint, text="go_home", command=go_home).pack()
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
#frame cancellation cnf setup
#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
Label(frame_cancellation_cnf, text="             ").pack()
Label(frame_cancellation_cnf, text="             ").pack()
Label(frame_cancellation_cnf, text="             ").pack()
Label(frame_cancellation_cnf, text="             ").pack()
Label(frame_cancellation_cnf, text="             ").pack()
Label(frame_cancellation_cnf, text="             ").pack()
Label(frame_cancellation_cnf, text="             ").pack()
cancel_cnf_label = Label(frame_cancellation_cnf)
cancel_cnf_label.pack()
Label(frame_cancellation_cnf, text="             ").pack()
Label(frame_cancellation_cnf, text="             ").pack()
Button(frame_cancellation_cnf, text="go home", command=go_home).pack()
#----------------------------------------------------------------------------------------------------------------
#frame login setup
#----------------------------------------------------------------------------------------------------------------
Label(frame_login, text="             ").pack()
Label(frame_login, text="             ").pack()
Label(frame_login, text="             ").pack()
Label(frame_login, text="             ").pack()
Label(frame_login, text="             ").pack()
Label(frame_login, text="             ").pack()
Label(frame_login, text="             ").pack()
Label(frame_login, text="             ").pack()
Label(frame_login, text="             ").pack()
Label(frame_login, text="             ").pack()
Label(frame_login, text="             ").pack()
Label(frame_login, text="             ").pack()
#taking inputs
user_name_entry = Entry(frame_login, width=20, justify="center")
password_entry = Entry(frame_login, width=20, justify="center")

#placeholder
user_name_entry.insert(0,"user_name")
password_entry.insert(0,"password")

#positioning
user_name_entry.pack()
password_entry.pack()
#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
#defining functions
#----------------------------------------------------------------------------------------------------------------
#login button assignment
def Login_Click():
	user_name_input = user_name_entry.get()
	password_input = password_entry.get()
	crsr.execute("SELECT * from user WHERE user_name = '%s' and password = '%s'" % (user_name_input, password_input))
	check = crsr.fetchone()
	if check:
		def Book_Click():
			#pay click defined
			def Pay_Click():
				def pay_cnf():
					crsr.execute("SELECT * from data")
					tup = crsr.fetchone()
					A_S = tup[0]
					W_L = tup[1]
					if (A_S > 0):
						status_insert = 'CNF'
						A_S = A_S - 1
						crsr.execute("UPDATE data SET A_S = %s" % (A_S))
						connection.commit()
					else:
						status_insert = 'WL' + str(W_L)
						W_L = W_L + 1
						crsr.execute("UPDATE data SET W_L = %s" % (W_L))
						connection.commit()
					crsr.execute("INSERT INTO tickets (user_name, name, age, gender, aadhar_no, phone_no, travel_date, train_no, source_stn, destination_stn, activity, status) VALUES(?,?,?,?,?,?,?,12345,'RPH', 'HWH', 'active', ?)", (user_name_entry.get(), passenger_name_entry.get(), age_entry.get(), gender_entry.get(), aadhar_no_entry.get(), phone_no_entry.get(),travel_date_entry.get(), status_insert, ))
					connection.commit()
					show_label.config(text="Ticket booked for " + passenger_name_entry.get() + ". Have a safe journey!!")
					raise_frame(frame_show)

				#passenger_name_input = passenger_name_entry.get()
				#if (card_no.get() != "") and (exp_date.get() != "") and (cvv.get() != ""):

				pay_cnf_btn.config(command=pay_cnf)
				raise_frame(frame_pay)
			crsr.execute("SELECT * from data")
			tup = crsr.fetchone()
			A_S = tup[0]
			W_L = tup[1]
			if (A_S > 0):
				booking_status.config(text="Booking status : AVAILABLE " + str(A_S))
				pay_btn.config(state="active")
			elif (W_L == 5):
				booking_status.config(text="NOT AVAILABLE")
				pay_btn.config(state="disabled")
			else:
				booking_status.config(text="Booking status : WAITING LIST " + str(W_L))
				pay_btn.config(state="active")
			pay_btn.config(command=Pay_Click)
			raise_frame(frame_fill)

		def Cancellation_Click():
			crsr.execute("SELECT * from tickets WHERE user_name = '%s'" % (user_name_entry.get()))
			tickets = crsr.fetchall()
			#print(len(tickets))
			i=0
			j=0
			for i in range(0, 6):
					for j in range(1, 13):
						l = Label(frame_cancellation, text="                                                                                   ")
						l.grid(row=i+17, column=0)
						l = Label(frame_cancellation, text="", width=12, borderwidth=2)
						l.grid(row=i+17, column=j)
			for i in range(0, len(tickets)):
				for j in range(1, 13):
					l = Label(frame_cancellation, text="                                                                                   ")
					l.grid(row=i+17, column=0)
					l = Label(frame_cancellation, text="" + str(tickets[i][j]), width=12, borderwidth=2, relief="groove")
					l.grid(row=i+17, column=j)

			def cancel_cnf():
				crsr.execute("SELECT * from data")
				tup = crsr.fetchone()
				A_S = tup[0]
				W_L = tup[1]
				#print(A_S)
				#print(W_L)
				if (A_S > 0 or W_L == 1):
					crsr.execute("UPDATE tickets SET status = 'CAN', activity = 'inactive' WHERE ticket_id = %s" % (cancel_entry.get()))
					connection.commit()
					crsr.execute("INSERT INTO cancel_tickets SELECT * FROM tickets WHERE ticket_id = %s" % (cancel_entry.get()))
					connection.commit()
					crsr.execute("DELETE FROM tickets WHERE ticket_id = %s" % (cancel_entry.get()))
					connection.commit()
					crsr.execute("UPDATE data SET A_S = %s" % (A_S + 1))
					connection.commit()
				else:
					crsr.execute("SELECT status from tickets WHERE ticket_id = %s" % (cancel_entry.get()))
					cancel_status_tup = crsr.fetchone()
					cancel_status = cancel_status_tup[0]
					print(cancel_status_tup)
					if (cancel_status == "CNF" and W_L > 1):
						crsr.execute("UPDATE Tickets SET status = 'CNF' WHERE status = 'WL1'")
						connection.commit()
						for i in range(2, W_L):
							status_insert = 'WL' + str(i-1) #value = "WL1"
							status_check = 'WL' + str(i) # value = "WL2"
							crsr.execute("UPDATE tickets SET status = '%s' WHERE status = '%s'" % (status_insert, status_check))
							connection.commit()
					elif (cancel_status != "CNF"):
						for i in range(int(cancel_status[-1])+1, W_L):
							status_check = 'WL' + str(i)
							status_insert = 'WL' + str(i-1)
							print(status_check)
							crsr.execute("UPDATE tickets SET status = '%s' WHERE status = '%s'" % (status_insert, status_check))
							connection.commit()
					crsr.execute("UPDATE tickets SET status = 'CAN', activity = 'inactive' WHERE ticket_id = %s" % (cancel_entry.get()))
					connection.commit()
					crsr.execute("INSERT INTO cancel_tickets SELECT * FROM tickets WHERE ticket_id = %s" % (cancel_entry.get()))
					connection.commit()
					crsr.execute("DELETE FROM tickets WHERE ticket_id = %s" % (cancel_entry.get()))
					connection.commit()
					crsr.execute("UPDATE data SET W_L = %s" % (W_L - 1))
					connection.commit()

				raise_frame(frame_cancellation_cnf)


			cancel_cnf_btn.config(command=cancel_cnf)
			raise_frame(frame_cancellation)

		def MyTickets_Click():
			def active_tickets():
				crsr.execute("SELECT * from tickets WHERE user_name = '%s'" % (user_name_entry.get()))
				tickets = crsr.fetchall()
				#print(len(tickets))
				i=0
				j=0
				for i in range(0, 6):
					for j in range(1, 13):
						l = Label(frame_active_tickets, text="                                                                                   ")
						l.grid(row=i+17, column=0)
						l = Label(frame_active_tickets, text="", width=12, borderwidth=2)
						l.grid(row=i+17, column=j)
				for i in range(0, len(tickets)):
					for j in range(1, 13):
						l = Label(frame_active_tickets, text="                                                                                   ")
						l.grid(row=i+17, column=0)
						l = Label(frame_active_tickets, text="" + str(tickets[i][j]), width=12, borderwidth=2, relief="groove")
						l.grid(row=i+17, column=j)
				raise_frame(frame_active_tickets)

			def inactive_tickets():
				crsr.execute("SELECT * from cancel_tickets WHERE user_name = '%s'" % (user_name_entry.get()))
				tickets = crsr.fetchall()
				#print(len(tickets))
				i=0
				j=0
				for i in range(0, 6):
					for j in range(1, 13):
						l = Label(frame_inactive_tickets, text="                                                                                   ")
						l.grid(row=i+17, column=0)
						l = Label(frame_inactive_tickets, text="", width=12, borderwidth=2)
						l.grid(row=i+17, column=j)
				for i in range(0, len(tickets)):
					for j in range(1, 13):
						l = Label(frame_inactive_tickets, text="                                                                                   ")
						l.grid(row=i+17, column=0)
						l = Label(frame_inactive_tickets, text="" + str(tickets[i][j]), width=12, borderwidth=2, relief="groove")
						l.grid(row=i+17, column=j)
				raise_frame(frame_inactive_tickets)

			active_ticket_btn.config(command=active_tickets)
			inactive_ticket_btn.config(command=inactive_tickets)
			raise_frame(frame_tickets)

		def Complaint_Click():
			def Complaint_Submit():
				complaint_text.delete('1.0', END)
			complaint_cnf_btn.config(command=Complaint_Submit)
			raise_frame(frame_complaint)

		label_main.config(text="hello "+ user_name_input)
		book_btn.config(command=Book_Click)
		cancel_btn.config(command=Cancellation_Click)
		tickets_btn.config(command=MyTickets_Click)
		complaint_btn.config(command=Complaint_Click)
		raise_frame(frame_dashboard)
	else:
		messagebox.showinfo("Rail", "Wrong Credentials")
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------
#end setup
#----------------------------------------------------------------------------------------------------------------
#login button
login_btn = Button(frame_login, text="Login", command=Login_Click)
login_btn.pack()


def Reg_Click():
	def Submit():
		crsr.execute("INSERT INTO user VALUES (?, ?)", (user_name_reg_entry.get(), password_reg_entry.get(),))
		connection.commit()
		raise_frame(frame_login)

	reg_cnf_btn.config(command=Submit)
	raise_frame(frame_register)

reg_btn = Button(frame_login, text="Register", command=Reg_Click)
reg_btn.pack()
#raising login frame
raise_frame(frame_login)

connection.commit() 

#connection.close()

root.mainloop()
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------