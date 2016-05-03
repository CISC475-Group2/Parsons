import React, { Component } from 'react'
import { connect } from 'react-redux'
import Problem from './Problem'

class App extends Component {
    render() {
        const { blocks, actions } = this.props
        return (
            <div>
                <Problem problemNumber={this.props.problemNumber}
                         compilesTo={this.props.compilesTo}
                         baseBlockString={this.props.baseBlockString}
                         baseBlock={this.props.baseBlock}
                         blocks={this.props.blocks}
                         onSwapBlocks={this.props.onSwapBlocks}
                         onMoveBlock={this.props.onMoveBlock}
                         onReset={this.props.onReset}
                         onSubmit={this.props.onSubmit} 
                         isSuccess={this.props.isSuccess} />
            </div>
        )
    }
}

function mapStateToProps(state) {
    return {
        problemNumber: state.problemNumber,
        compilesTo: state.compilesTo,
        baseBlockString: state.baseBlockString,
        baseBlock: state.blocks[0],
        isSuccess: state.lastAttempt.isSuccess,
        blocks: state.blocks.slice(1, state.blocks.length)
    }
}

function mapDispatchToProps(dispatch) {
    return {
        onSwapBlocks: (sourceId, targetId) => {
            dispatch({ type: 'SWAP_BLOCKS', sourceId: sourceId, targetId: targetId })
        },
        onMoveBlock: (sourceId, targetId) => {
            dispatch({ type: 'MOVE_BLOCK', sourceId: sourceId, targetId: targetId })
        },
        onReset: () => {
            dispatch({ type: 'RESET' })
        },
        onSubmit: () => {
            dispatch({ type: 'SUBMIT' })
        }
    }
}

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(App)
