<?php

include('command.php');

	class clienthandler{

		private $islogin;

		public function __construct(command $command){
		}

		public function isloggedin() {
			return $this->islogin;
		}

		public function loggedin() {

			$this->islogin = true;

		}
	}

?>

