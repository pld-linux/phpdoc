Summary:	phpdoc - adoption of Javadoc to the PHP world
Summary(pl.UTF-8):	phpdoc - adaptacja Javadoc dla świata PHP
Name:		phpdoc
Version:	1.0beta
Release:	0.8
Epoch:		0
License:	LGPL
Group:		Applications/WWW
Source0:	http://www.phpdoc.de/download/%{name}1beta.zip
# Source0-md5:	ca05fe9e0bb6171b2defee60a23e98c9
URL:		http://www.phpdoc.de/
BuildRequires:	sed >= 4.0
Requires:	php(pcre)
Requires:	php(xml)
Requires:	webserver(php) >= 4.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
PHPDoc is an adoption of Javadoc to the PHP world. PHPDoc is written
in PHP. It offers you a way to generate an API documentation of object
oriented and procedural code with certain markup in your source.

%description -l pl.UTF-8
PHPDoc to adaptacja Javadoc dla świata PHP. PHPDoc jest napisany w
PHP. Oferuje sposób generowania dokumentacji API kodu zorientowanego
obiektowo oraz proceduralnego z określonymi znacznikami w źródłach.

%prep
%setup -q -n PHPDoc
find -name CVS | xargs rm -rf
mv apidoc/keep/index{2,}.html

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a . $RPM_BUILD_ROOT%{_appdir}

# in doc
rm -f $RPM_BUILD_ROOT%{_appdir}/README

sed -i -e '
	s,c:/www/apache/doc,%{_appdir},g;
	s,c:/,/,g;
	s,define("LINEBREAK", "\r\n"),define("LINEBREAK", "\n"),
	s,include("./prepend.php");.*,include PHPDOC_INCLUDE_DIR. "/prepend.php";,
' $RPM_BUILD_ROOT%{_appdir}/index.php

cat >README.PLD <<'EOF'
For quick startup You should copy %{_appdir}/index.php
and setup source directory / output directory:

$doc->setSourceDirectory("/www/apache/form/");
$doc->setTarget("/www/apache/doc/apidoc/");

You also need to copy %{_appdir}/apidoc/keep/* to the direcory you set
with setTarget.

for complete usage instructions read:
http://www.phpdoc.de/doc/usage.html

You may also read in case of troubles:
http://www.phpdoc.de/doc/installation.html

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.PLD
%{_appdir}
