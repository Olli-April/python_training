import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, homephone=home,
                                    mobilephone=mobile, workphone=work, email=email, email2=email2, email3=email3, secondaryphone=phone2))
        finally:
            cursor.close()
        return list

    def get_contacts_not_in_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select y.id, y.firstname, y.lastname, y.address, y.home, y.mobile, y.work, y.email, y.email2, y.email3, y.phone2 from addressbook y left join address_in_groups cg on cg.id=y.id where cg.id is null")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, homephone=home,
                            mobilephone=mobile, workphone=work, email=email, email2=email2, email3=email3, secondaryphone=phone2))
        finally:
            cursor.close()
        return list

    def get_contacts_in_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select distinct y.id, y.firstname, y.lastname, y.address, y.home, y.mobile, y.work, y.email, y.email2, y.email3, y.phone2 from addressbook y inner join address_in_groups cg on cg.id=y.id")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, homephone=home,
                                    mobilephone=mobile, workphone=work, email=email, email2=email2, email3=email3,
                                    secondaryphone=phone2))
        finally:
            cursor.close()
        return list

    def get_groups_wth_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select g.group_id, g.group_name, g.group_header, g.group_footer from group_list g join address_in_groups ga on ga.group.id=g.group_id join addressbook ab on ab.id=ga.id")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

