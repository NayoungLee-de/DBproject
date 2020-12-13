DROP TABLE IF EXISTS management;
DROP TABLE IF EXISTS register;
DROP TABLE IF EXISTS member;
DROP TABLE IF EXISTS trainer;

CREATE TABLE member(
	mNum INTEGER NOT NULL,
	mName VARCHAR(80),
	sex CHAR(4),
	bDate CHAR(6),
	phoneNum CHAR(20),
	userId TEXT,
	userPw TEXT,
    PRIMARY KEY(mNum)
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
    PRIMARY KEY(mNum, tNum),
	FOREIGN Key(mNum) REFERENCES member(mNum) on DELETE CASCADE on UPDATE CASCADE,
	FOREIGN Key(tNum) REFERENCES member(tNum) on DELETE CASCADE on UPDATE CASCADE
);

CREATE TABLE register(
	mNum INTEGER NOT NULL,
	month CHAR(4),
	rDate CHAR(8),
	FOREIGN Key(mNum) REFERENCES member(mNum) on DELETE CASCADE on UPDATE CASCADE
);