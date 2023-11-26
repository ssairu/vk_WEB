package com.example.first_vk_app

import android.content.res.Configuration
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.GridLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.first_vk_app.databinding.ActivityMainBinding


class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private lateinit var rvAdapter: RvAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val layoutManager: RecyclerView.LayoutManager =
            if (resources.configuration.orientation == Configuration.ORIENTATION_LANDSCAPE) {
                GridLayoutManager(this, resources.getInteger(R.integer.LANDSCAPE_COLS))
            } else {
                GridLayoutManager(this, resources.getInteger(R.integer.PORTRAIT_COLS))
            }
        binding.recyclerRectangle.layoutManager = layoutManager
        var count = resources.getInteger(R.integer.PER_PAGE_ITEMS)

        savedInstanceState?.let { bundle ->
            count = bundle.getInt("COUNT_RECT")
        }
        rvAdapter = RvAdapter(count)
        binding.recyclerRectangle.adapter = rvAdapter
        binding.addButton.setOnClickListener {
            rvAdapter.addRectangle()
        }
    }


    override fun onSaveInstanceState(outState: Bundle) {
        outState.run {
            outState.putInt("COUNT_RECT", binding.recyclerRectangle.adapter!!.itemCount)
        }
        super.onSaveInstanceState(outState)
    }
}