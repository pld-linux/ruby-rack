%define pkgname rack
Summary:	Modular interface to webservers
Summary(pl.UTF-8):	Modularny interfejs do serwerów WWW
Name:		ruby-%{pkgname}
Version:	1.2.1
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://chneukirchen.org/releases/%{pkgname}-%{version}.tar.gz
# Source0-md5:	b427cf90880ff91eeae97c576b5c0c2a
URL:		http://rubyforge.org/projects/rack
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
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
oprogramowania znajdującego się między nimi (tzw. middleware) w jedno
wywołanie metody.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%{__sed} -i -e 's|/usr/bin/env ruby|%{__ruby}|' bin/rackup

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
%{__rm} -fr ri/{FCGI,created.rid,cache.ri}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog example/*
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/rack
%{ruby_rubylibdir}/rack.rb

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Rack
