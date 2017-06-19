class User(db.Model):
	# __bind_key__ = 'local'
	def __init__(self, username, database):
        User.__init__(self, username)
        Database.__init__(self, database)


	id = db.Column(db.Integer, primary_key = True, autoincrement =True)
	first_name = db.Column(db.String(254))
	# last_name = db.Column(db.String(254))
	access = db.Column(db.String(254))
	email = db.Column(db.String(254), unique=True)


	_password = db.Column(db.String(254))

	# Flag for session management
	authenticated = db.Column(db.Boolean, default=False)

	#Flag for email verification
	email_confirmed = db.Column(db.Boolean, default=False)
    
	# .password hybrid property
	@hybrid_property
	def password(self):
		return self._password

	# Hashing the password once and for all
	@password.setter
	def _set_password(self,plaintext):
		self._password = bcrypt.generate_password_hash(plaintext)

	# Password Matching
	def is_password_correct(self,plaintext):
		return bcrypt.check_password_hash(self._password, plaintext)


	# Methods required for Flask-Login to work

	def is_active(self):
		return True

	def get_id(self):
		return unicode(self.id)

	def is_authenticated(self):
		return self.authenticated

	def is_anonymous(self):
		return False


	def __repr__(self):
		return 'User : {}'.format(self.first_name)
