filter ToIndent {
	% { $_ -replace "^(.*[+,\\\\]-.*)$","$&\" } |
	% { $_ -replace "\|   " ,"`t" }  |
	% { $_ -replace "\+---" ,"`t" }  |
	% { $_ -replace "\\---" ,"`t" }  |
	% { $_ -replace "    "  ,"`t" }  |
	% { If ( $_ -notmatch "`t+$" ){$_} }
}