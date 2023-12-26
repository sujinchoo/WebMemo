{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "421ff47b",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, request, redirect, url_for\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "notes = []\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return render_template('index.html', notes=notes)\n",
    "\n",
    "@app.route('/add_note', methods=['POST'])\n",
    "def add_note():\n",
    "    note = request.form.get('note')\n",
    "    notes.append(note)\n",
    "    return redirect(url_for('index'))\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
