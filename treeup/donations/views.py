from flask import Blueprint, g, render_template, request, url_for, redirect
from treeup.donations.models import Donation
import stripe
from treeup import db
from sqlalchemy import func
from config import CHARITY, MISSION, TAGLINE, LOGO_URL

mod = Blueprint("general", __name__)

from treeup import stripe_keys

@mod.route("/")
def home():
    show_all = request.args.get("all", False)
    goal = 10000
    raised = 1000
    donations = Donation.query.order_by(Donation.date_created.desc())
    if not show_all:
        donations = donations.limit(10)
    donations = donations.all()
    raised = Donation.query.with_entities(func.sum(Donation.amount)).first()
    if raised:
        raised = raised[0]
        raised = raised / 100.0
    else:
        raised = 0
    return render_template("home.html", charity=CHARITY, mission=MISSION,
                            logo=LOGO_URL, goal=goal,
                            raised=raised, tagline=TAGLINE, donations=donations)

@mod.route("/donate/")
def donate():
    return render_template("donate.html", key=stripe_keys['publishable_key'], charity=CHARITY, logo=LOGO_URL)


@mod.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    amount = request.form['dAmount']
    if amount.startswith("$"):
        amount = amount[1:]
    amount = int(float(amount) * 100)
    customer = stripe.Customer.create(
        email='test@aol.com',
        card=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )
    d = Donation()
    d.name = request.form.get("donorName", "Anonymous")
    if not d.name:
        d.name = "Anonymous"
    d.email = customer.email
    d.amount = amount
    d.message = request.form.get("message", "")

    db.session.add(d)
    db.session.commit()
    # return redirect("/thankyou")
    return render_template('charge.html', amount=amount, charity=CHARITY, logo=LOGO_URL)
