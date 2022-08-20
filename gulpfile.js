// Constantes de gulp
const { src, dest, watch, parallel } = require('gulp');

// CSS and SASS
const sass = require('gulp-sass')(require('sass'));

// Imagenes.
const gulpAvif = require('gulp-avif');
const webp = require('gulp-webp');

// Automatizacion JS.
const terser = require('gulp-terser-js');

function myscss( done ){
    src('static/scss/**/*.scss')
        .pipe( sass() )
        .pipe( dest('static/css') )
    done();
}

function javascript( done ){
    src('src/js/**/*.js')
        .pipe( terser() )
        .pipe( dest('static/js'))
    done();
}

function imagesWebp( done ){
    const options = {
        quality: 50
    }
    src('src/images/**/*.{jpg,png}')
        .pipe( webp(options) )
        .pipe( dest('static/img/imgProcess') )
    done();
}

function imagesAvif( done ){
    const options = {
        quality: 50
    }
    src('src/images/**/*.{jpg,png}')
        .pipe( gulpAvif(options) )
        .pipe( dest('static/img/imgProcess') )
    done();
}

function watches( done ){
    watch('static/scss/**/*.scss', myscss);
    watch('src/js/**/*.js', javascript);
    done();
}



exports.watches = parallel(watches, javascript,imagesWebp, imagesAvif);