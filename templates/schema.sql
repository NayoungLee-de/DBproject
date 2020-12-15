DROP TABLE IF EXISTS management;
DROP TABLE IF EXISTS register;
DROP TABLE IF EXISTS member;
DROP TABLE IF EXISTS trainer;

CREATE TABLE member(
	mNum INTEGER PRIMARY KEY AUTOINCREMENT,
	mName TEXT,
	sex CHAR(4),
	bDate CHAR(6),
	phoneNum VARCHAR(30),
	userId TEXT,
	userPw TEXT
);

CREATE TABLE trainer (
	tNum INTEGER NOT NULL,
	tName VARCHAR(80),
	sex CHAR(4),
    PRIMARY KEY(tNum)
);

CREATE TABLE management(
	mNum INTEGER NOT NULL,
	tNum INTEGER NOT NULL,
	attend CHAR(8),
	FOREIGN Key(mNum) REFERENCES member(mNum) on DELETE CASCADE on UPDATE CASCADE,
	FOREIGN Key(tNum) REFERENCES trainer(tNum) on DELETE CASCADE on UPDATE CASCADE
);
