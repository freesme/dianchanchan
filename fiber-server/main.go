package main

import (
	"fiber-server/global"
	"fiber-server/initialize"
)

func main() {
	initialize.Init()
	global.GORM_DB.Exec("INSERT INTO sessions(k, v, e) VALUES (5,422123,5)")
}
