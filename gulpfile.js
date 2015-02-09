var gulp            = require('gulp'),
    coffee          = require('gulp-coffee'),
    sass            = require('gulp-sass'),
    minifycss       = require('gulp-minify-css'),
    haml            = require('gulp-haml'),
    minifyhtml      = require('gulp-minify-html'),
    livereload      = require('gulp-livereload'),
    notify          = require('gulp-notify'),
    watch           = require('gulp-watch'),
    fs              = require("fs"),
    rename          = require("gulp-rename"),
    plumber         = require('gulp-plumber');
 
var paths = {
    'sassDirs': [],
    'hamlDirs': [],
    'coffeescriptDirs': []
};
 
var dive = function (dir, action) {
    if (typeof action !== "function")
    action = function (error, file) { };
    fs.readdir(dir, function (err, list) {
    if (err)
        return action(err)
        list.forEach(function (file) {
            var path = dir + "/" + file;
            fs.stat(path, function (err, stat) {
                if (stat && stat.isDirectory()) {
                    dive(path, action);
                    action(path);
                }
            });
        });
    });
};
 
var checkDirName = function(path) {
    var dirName = path.substring(path.lastIndexOf('/'), path.length);
    path = path.substring(2);
    if(dirName == '/sass') {
        paths.sassDirs.push(path + '/*.sass');
    } else if (dirName == '/haml') {
        paths.hamlDirs.push(path + '/*.haml');
    } else if (dirName == '/coffee') {
        paths.coffeescriptDirs.push(path + '/*.coffee');
    }
}
 
gulp.task('analyseDirs', function() {
    dive('.', checkDirName);
});
 
function watchCoffee() {
    watch({glob: paths.coffeescriptDirs, base: './', emitOnGlob: false}, function(files) {
        return files
            .pipe(notify("Syncing <%= file.relative %>!"))
            .pipe(plumber({errorHandler: notify.onError("COFFEE ERROR: <%= error.message %>")}))
            .pipe(coffee())
            .pipe(rename(function (path) {
                path.dirname += "/../js";
            }))
            .pipe(plumber.stop())
            .pipe(gulp.dest(''))
            .pipe(livereload());
    });
}
 
function watchSass() {
    watch({glob: paths.sassDirs, base: './', emitOnGlob: false}, function(files) {
        return files
            .pipe(notify("Syncing <%= file.relative %>!"))
            .pipe(plumber({errorHandler: notify.onError("SASS ERROR: <%= error.message %>")}))
            .pipe(sass({ sourceComments: "normal"}))
            .pipe(minifycss())
            .pipe(rename(function (path) {
                path.dirname += "/../css";
            }))
            .pipe(plumber.stop())
            .pipe(gulp.dest(''))
            .pipe(livereload());
    });
}
 
function watchHaml() {
    watch({glob: paths.hamlDirs, base: './', emitOnGlob: false}, function(files) {
        return files
            .pipe(notify("Syncing <%= file.relative %>!"))
            .pipe(plumber({errorHandler: notify.onError("HAML ERROR: <%= error.message %>")}))
            .pipe(haml())
            .pipe(minifyhtml())
            .pipe(rename(function (path) {
                path.dirname += "/../";
            }))
            .pipe(plumber.stop())
            .pipe(gulp.dest(''))
            .pipe(livereload());
    });
}
 
function watchPython() {
    watch({glob: '**/*.py', emitOnGlob: false}, function(files) {
        setTimeout(function(){
            return files
                .pipe(notify("Syncing <%= file.relative %>!"))
                .pipe(livereload());
        },1000);
    });
}
 
gulp.task('startLiveReload', function() {
    gulp.src('')
        .pipe(notify("Starting LiveReload"))
        .pipe(livereload());
});
 
gulp.task('watch',['analyseDirs', 'startLiveReload'], function() {
    setTimeout(function(){
        watchSass();
        watchCoffee();
        watchPython();
        watchHaml();
    }, 1000);
});
 
gulp.task('default',['watch'])