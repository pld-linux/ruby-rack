Summary:	Modular interface to webservers
Summary(pl.UTF-8):	Modularny interfejs do serwerów WWW
Name:		ruby-rack
Version:	0.1.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://chneukirchen.org/releases/rack-%{version}.tar.gz
# Source0-md5:	79b46158b7b30adcd7a9148cc7ed4305
URL:		http://rubyforge.org/projects/rack
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
#BuildArch:	noarch
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rack provides a minimal, modular and adaptable interface for
developing web applications in Ruby. By wrapping HTTP requests and
responses in the simplest way possible, it unifies and distills the
API for web servers, web frameworks, and software in between (the
so-called middleware) into a single method call.

%description -l pl.UTF-8
Rack dostarcza minimalny, modularny i adaptowalny interfejs do
tworzenia aplikacji WWW w języku Ruby. Opakowując zapytania i
odpowiedzi HTTP w sposób najprostszy z możliwych, unifikuje oraz
przekształca API dla serwerów WWW, szkieletów aplikacji WWW i
oprogramowania znajdującego się między nimi (tzw. middleware) w
jedno wywołanie metody.

%prep
%setup -q -n rack-%{version}

%build
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc lib SPEC

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc README AUTHORS example/*
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/rack
%{ruby_rubylibdir}/rack.rb
