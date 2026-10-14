
# INF601 - Advanced Programming in Python
# Adeola Ajayi
# Mini Project 5

from flask import (
    Blueprint, flash, g, redirect,
    render_template, request, url_for
)

from werkzeug.exceptions import abort

from helpdesk.auth import login_required
from helpdesk.db import get_db

bp = Blueprint("tickets", __name__, url_prefix="/tickets")


@bp.route("/")
@login_required
def index():
    db = get_db()

    tickets = db.execute(
        "SELECT t.id, t.title, t.description, "
        "t.priority, t.status, t.created, "
        "t.user_id, u.username "
        "FROM tickets t "
        "JOIN users u ON t.user_id = u.id "
        "WHERE t.user_id = ? "
        "ORDER BY t.created DESC",
        (g.user["id"],)
    ).fetchall()

    return render_template("tickets/index.html", tickets=tickets)



@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        title = request.form["title"].strip()
        description = request.form["description"].strip()
        priority = request.form.get("priority", "Medium")

        error = None

        if not title:
            error = "Ticket title is required."
        elif not description:
            error = "Ticket description is required."
        elif priority not in ("Low", "Medium", "High"):
            error = "Invalid ticket priority."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                """
                INSERT INTO tickets
                (user_id, title, description, priority)
                VALUES (?, ?, ?, ?)
                """,
                (g.user["id"], title, description, priority),
            )
            db.commit()

            flash("Support ticket created successfully!")
            return redirect(url_for("tickets.index"))

    return render_template("tickets/create.html")


