import sys
import sqlite3 as sql
import guiWindow



def main():
    # Main database stuff here
    conn = sql.connect('north_star_practice_db.db')
    cursor = conn.cursor()
    # get_info(cursor, id) # May want to consider including this in GUI
    app = mainMenu.QApplication(sys.argv)
    ex = mainMenu.Window(conn, cursor)
    ex.isHidden()
    sys.exit(app.exec_())


main()
