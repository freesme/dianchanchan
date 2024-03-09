package initialize

import (
	"fmt"
	"github.com/joho/godotenv"
	"log"
	"os"
)

func Init() {
	loadConfig()
	if os.Getenv("MODULE") == "sqlite" {
		sqliteInit()
	}

}

func loadConfig() {

	curr := os.Getenv("GO_ENV")
	if curr == "" {
		curr = "dev" // 默认值
	}

	// 构建.env文件的名称，基于当前环境
	envFileName := fmt.Sprintf(".env.%s", curr)
	fmt.Println("Loading config file: ", envFileName)

	// 加载指定的.env文件
	err := godotenv.Load(envFileName)
	if err != nil {
		log.Fatalf("Error loading %s file: %v", envFileName, err)
	}

	// 从加载的环境变量中读取一个值，作为示例
	someConfig := os.Getenv("SOME_CONFIG")
	fmt.Println("SOME_CONFIG: ", someConfig)
}
