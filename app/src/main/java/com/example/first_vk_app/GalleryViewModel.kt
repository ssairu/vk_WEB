package com.example.first_vk_app

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel

class GalleryViewModel : ViewModel() {
    var PictureList : MutableLiveData<MutableList<PictureItem>> = MutableLiveData()

    init {
        PictureList.value = mutableListOf(
            PictureItem(0, "name 0", "path 0", "date 0"),
            PictureItem(1, "name 1", "path 1", "date 1"),
            PictureItem(2, "name 2", "path 2", "date 2"),
            PictureItem(3, "name 3", "path 3", "date 3"),
            PictureItem(4, "name 4", "path 4", "date 4"),
        )
    }

    fun getListPictures() = PictureList

    fun addPicture() {
        var i = PictureList.value?.size
        i?.let { PictureItem(it, "name $i", "path $i", "date $i") }?.let {
            PictureList.value?.add(
                it
            )
        }
    }

    // TODO: Implement the ViewModel
}