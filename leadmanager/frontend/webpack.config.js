module.exports={
    module:{
        rules:{
            test:/\.js$/,
            exlude: /node_modules/,
            use:{
                loader:"babel-loader"
            }
        }
    }
}