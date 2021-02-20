let { merge } = require('webpack-merge');
let webpack = require('webpack');
let CopyWebpackPlugin = require('copy-webpack-plugin');
let MiniCssExtractPlugin = require('mini-css-extract-plugin');
let OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
let TerserPlugin = require('terser-webpack-plugin');

let common = {
  watchOptions: {
    poll: (process.env.WEBPACK_WATCHER_POLL || 'true') === 'true'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: [/node_modules/],
        enforce: "pre",
        use: [
            'babel-loader',
            'source-map-loader'
        ],
      },
      {
        test: [/\.scss$/, /\.css$/],
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'postcss-loader',
          'sass-loader'
        ]
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        exclude: /fonts/,
        loader: 'file-loader?name=/images/[name].[ext]'
      },
      {
        test: /\.(ttf|eot|svg|woff2?)$/,
        exclude: /images/,
        use: [{
          loader: 'file-loader',
          options: {
            name: '[name].[ext]',
            outputPath: 'fonts/',
            publicPath: '../fonts'
          }
        }]
      }
    ]
  },
  optimization: {
    minimizer: [
      new TerserPlugin({cache: true, parallel: true, sourceMap: false}),
      new OptimizeCSSAssetsPlugin({})
    ]
  }
};

module.exports = [
  merge(common, {
    entry: [
      __dirname + '/app/app.scss',
      __dirname + '/app/app.js'
    ],
    output: {
      path: __dirname + '/../public',
      filename: 'js/app.js'
    },
    resolve: {
      modules: [
        __dirname + '/node_modules',
        __dirname + '/app'
      ]
    },
    plugins: [
      new CopyWebpackPlugin({patterns: [{from: __dirname + '/static'}]}),
      new MiniCssExtractPlugin({filename: 'css/app.css'}),
      new webpack.ProvidePlugin({$: 'jquery', jQuery: 'jquery'})
      // new webpack.SourceMapDevToolPlugin({
      //   filename: 'popper.js.map',
      //   exclude: ['popper.js.map']
      // })
    ]
  })
];
