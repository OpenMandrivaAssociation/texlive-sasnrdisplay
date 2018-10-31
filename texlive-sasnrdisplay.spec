Name:		texlive-sasnrdisplay
Version:	0.95
Release:	2
Summary:	Typeset SAS or R code or output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sasnrdisplay
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sasnrdisplay.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sasnrdisplay.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The SASnRdisplay package serves as a front-end to the listings,
which permits statisticians and others to import source code,
and the results of their calculations or simulations into LaTeX
projects. The package is also capable of overloading the Sweave
and SASweave packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sasnrdisplay
%doc %{_texmfdistdir}/doc/latex/sasnrdisplay

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
