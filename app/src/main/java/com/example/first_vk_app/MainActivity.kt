package com.example.first_vk_app

import android.content.res.Configuration
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.PersistableBundle
import androidx.recyclerview.widget.GridLayoutManager
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.first_vk_app.databinding.ActivityMainBinding


class MainActivity : AppCompatActivity() {

    // view binding for the activity
    private var _binding: ActivityMainBinding? = null
    private val binding get() = _binding!!

    private lateinit var rvAdapter: RvAdapter
    var count = 6

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        _binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // create  layoutManager
        val layoutManager: RecyclerView.LayoutManager
        if (resources.configuration.orientation == Configuration.ORIENTATION_LANDSCAPE){
            layoutManager = GridLayoutManager(this, 4)
        } else {
            layoutManager = GridLayoutManager(this, 3)
        }

        // pass it to rvLists layoutManager
        binding.recyclerRectangle.setLayoutManager(layoutManager)

        // initialize the adapter,
        // and pass the required argument

        savedInstanceState?.let { bundle ->
            count = bundle.getInt("COUNT_RECT")
        }

        rvAdapter = RvAdapter(count)

        // attach adapter to the recycler view
        binding.recyclerRectangle.adapter = rvAdapter
        binding.addButton.setOnClickListener {
            rvAdapter.addRectangle()
        }
    }


    // on destroy of view make
    // the binding reference to null
    override fun onDestroy() {
        super.onDestroy()
        _binding = null
    }


    override fun onSaveInstanceState(outState: Bundle) {

        outState.run {
            outState.putInt("COUNT_RECT", binding.recyclerRectangle.adapter!!.itemCount)
        }

        super.onSaveInstanceState(outState)
    }
}