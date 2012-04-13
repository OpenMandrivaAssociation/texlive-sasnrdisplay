# revision 25751
# category Package
# catalog-ctan /macros/latex/contrib/sasnrdisplay
# catalog-date 2012-03-27 17:23:43 +0200
# catalog-license lppl1.3
# catalog-version 0.91
Name:		texlive-sasnrdisplay
Version:	0.91
Release:	1
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
%{_texmfdistdir}/tex/latex/sasnrdisplay/SASnRdisplay.cfg
%{_texmfdistdir}/tex/latex/sasnrdisplay/SASnRdisplay.sty
%doc %{_texmfdistdir}/doc/latex/sasnrdisplay/README
%doc %{_texmfdistdir}/doc/latex/sasnrdisplay/SASnRdisplay.pdf
%doc %{_texmfdistdir}/doc/latex/sasnrdisplay/SASnRdisplay.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
