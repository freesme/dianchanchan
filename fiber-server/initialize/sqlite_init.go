package initialize

import (
	"fiber-server/global"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
	"log"
)

func sqliteInit() {
	db, err := gorm.Open(sqlite.Open("sqlite.db"), &gorm.Config{})
	if err != nil {
		log.Fatalln("gorm open err:", err)
	}
	global.GORM_DB = db
}
